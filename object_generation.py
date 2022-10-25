import numpy as np

class Rectangle():

    def __init__(self, grid_height, grid_width, random_size=True, height=-1, width=-1, random_color=True, color=None, 
                colors_dict={'black':0, 'blue':1, 'red':2, 'green':3, 'yellow':4, 'gray':5, 'pink':6, 'orange':7, 'light_blue':8, 'purple':9}):

        
        self.grid_height = grid_height
        self.grid_width = grid_width
        self.max_shape_to_grid_ratio = 0.5
        self.satisfied=False

        self.height=height
        self.width=width

        if random_size:
            while not self.satisfied:
                self.height = np.random.randint(1, 30)
                self.width = np.random.randint(1, 30) #randomly generates size of the rectangle

                if self.height*self.width<=self.max_shape_to_grid_ratio*self.grid_height*self.grid_width: #checks whether it fits in the grid
                    self.satisfied=True
        
        self.vertical_symmetry=True
        self.horizontal_symmetry=True
        self.diagonal_symmetry=True

        self.color=color

        if random_color:
            self.color=np.random.randint(1,9, size=1) #color choice (we avoid choosing black)

        
    def generate_rectangle(self, grid, upper_left_x_coordinate, upper_left_y_coordinate): #modify the grid to create the rectangle
            
        #upper_left_x_coordinate: coordinate of upper_left corner of the rectangle

        self.upper_left_x_coordinate=upper_left_x_coordinate
        self.upper_left_y_coordinate=upper_left_y_coordinate #store the coordinates in the class, because it will be useful to have them saved when we define transformations 

        if (upper_left_x_coordinate<0) or (upper_left_x_coordinate+self.width>self.grid_width) or (upper_left_y_coordinate<0)or (upper_left_y_coordinate+self.height>self.grid_height):

            print('dimensions do not agree with coordinates specifications')
            return grid

            

        for i in range(upper_left_y_coordinate, upper_left_y_coordinate+self.height):
            for j in range(upper_left_x_coordinate, upper_left_x_coordinate+self.width):

                grid[i, j]=self.color
        
        return grid
    
    def erase_rectangle(self, grid):
        
        for i in range(self.upper_left_y_coordinate, self.upper_left_y_coordinate+self.height):
            for j in range(self.upper_left_x_coordinate, self.upper_left_x_coordinate+self.width):
                grid[i, j]=0
        
        return grid
    
    def translation(self, grid, shift_right, shift_down):

        #shift right and shift left can take negative values, which corresponds to shift left and shift 

        if (self.upper_left_x_coordinate+shift_right<0)or(self.upper_left_x_coordinate+shift_right+self.width>self.grid_width)or(self.upper_left_y_coordinate+shift_down<0)or(self.upper_left_y_coordinate+shift_down+self.height>self.grid_height):

            print('translation not possible due to dimension issues')
            return grid
        
        grid=self.erase_rectangle(grid)

        #translation is equivalent to generating a new rectangle with shifted coordinates
        return self.generate_rectangle(grid, self.upper_left_x_coordinate+shift_right, self.upper_left_y_coordinate+shift_down) 

    
    '''def rotation(self, grid, angle):

        #the angle is intended here as anti-clockwise rotations

        if angle not in [0, 90, 180, 270]:

            print('specified angle not available')
            return grid

        if angle==0:
            return grid
        
        if angle==90:'''


        





